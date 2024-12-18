package main

import (
	"bufio"
	"context"
	"encoding/json"
	"fmt"
	"os"
	"strings"

	"github.com/open-policy-agent/opa/rego"
	"github.com/open-policy-agent/opa/topdown"
)

func main() {
	fmt.Println("[!] Bienvenue chez OPain / Welcome to OPain")
	fmt.Println("      Fraichement Baked")
	fmt.Println("           Organic Pain")
	fmt.Println("")
	fmt.Println("What would you like to order?")
	breads, _ := GetBreads()

	for i, bread := range breads {
		fmt.Printf("      %d. %s\n", i+1, bread)
	}

	fmt.Printf("[?] Selection (%d-%d): ", 1, len(breads))

	var breadIdx int
	fmt.Scanln(&breadIdx)

	if breadIdx < 1 || breadIdx > len(breads) {
		fmt.Println("Invalid selection")
		return
	}

	breadIdx -= 1

	fmt.Printf("[?] How many `%s` would like? (1-100) ", breads[breadIdx])
	var qty int
	fmt.Scanln(&qty)

	fmt.Printf("[?] Who is this order for? Please enter your name or business: ")

	reader := bufio.NewReader(os.Stdin)
	name, _ := reader.ReadString('\n')
	name = name[:len(name)-1]

	order, err := CreateOrder(breads[breadIdx], qty, name)
	if err != nil {
		fmt.Println("[!] An error occured and your order could not be created.")
		fmt.Println(err.Error())
		return
	}

	fmt.Printf("[!] Your order was created.\n")
	fmt.Printf("    total: $%d\n", order.Total)
	fmt.Printf("    notes: %s.\n", order.Notes)
}

type Order struct {
	Total int    `json:"total"`
	Notes string `json:"notes"`
}

// GetBreads returns the list of available breads
func GetBreads() ([]string, error) {
	var result []string
	doc := NewRegoDocument("data", "opain", "breads")
	err := EvalQuery(doc, &result)
	return result, err
}

// CreateOrder creates an order for the given bread
func CreateOrder(bread string, qty int, name string) (Order, error) {
	var result Order
	fn := NewRegoDocument("data", "opain", "create_order").
		AsFunction().
		Arg(bread).
		Arg(qty).
		Arg(name)

	err := EvalQuery(fn, &result)
	return result, err
}

var opainRego string = `
package opain

import rego.v1

max_quantity := 100

discounts["Chef Bonappletea"] = 0.5

discounts["FLAG-redacted"] = 1.0

breads contains bread if prices[bread]

prices["Baguette"] = 3

prices["Focaccia"] = 5

prices["Croissant"] = 1

prices["Loaf"] = 4

prices["Bagel"] = 2

prices["Gâteaux aux fruits"] = 10

create_order(bread, qty, name) = {
	"total": total,
	"notes": notes,
} if {
	qty > 0
	qty <= max_quantity
	not discounts[name]
	total := prices[bread] * qty
	notes := sprintf("Thank you for your order '%s'!", [name])
}

create_order(bread, qty, name) = {
	"total": total,
	"notes": notes,
} if {
	qty > 0
	qty <= max_quantity
	order_discount := discounts[name]
	total := (prices[bread] * qty) * (1 - order_discount)
	notes := sprintf("Applied %d%% discount for '%s'!", [order_discount * 100, name]) 
}
`

func EvalQuery(query AsRego, result interface{}) error {
	q, err := query.Rego()
	if err != nil {
		return err
	}
	r := rego.New(
		rego.Module("opain.rego", opainRego),
		rego.Query(q),
		rego.EnablePrintStatements(true),
		rego.PrintHook(topdown.NewPrintHook(os.Stdout)),
	)

	rs, err := r.Eval(context.Background())
	if err != nil {
		return err
	}
	if len(rs) == 0 {
		return fmt.Errorf("empty result set")
	}

	j, _ := json.Marshal(rs[0].Expressions[0].Value)
	return json.Unmarshal(j, result)
}

// Rego Query Builder
type AsRego interface {
	Rego() (string, error)
}

// Path to a Rego document
type RegoDocument struct {
	Path []string
}

// Rego function call
type RegoFunction struct {
	Path RegoDocument
	Args []AsRego
}

// Rego scalar (int, string)
type RegoScalar struct {
	Value interface{}
}

// Convert a RegoDocument to a Rego string query
func (r RegoDocument) Rego() (string, error) {
	return strings.Join(r.Path, "."), nil
}

// Convert a RegoFunction to a Rego string query
func (r RegoFunction) Rego() (string, error) {
	fn, err := r.Path.Rego()
	if err != nil {
		return "", err
	}
	args := []string{}
	for _, arg := range r.Args {
		s, err := arg.Rego()
		if err != nil {
			return "", err
		}
		args = append(args, s)
	}

	return fmt.Sprintf("%s(%s)", fn, strings.Join(args, ", ")), nil
}

// Convert a RegoScalar to a Rego string query
func (r RegoScalar) Rego() (string, error) {
	switch r.Value.(type) {
	case int:
		return fmt.Sprintf("%d", r.Value), nil
	case string:
		return fmt.Sprintf(`"%s"`, r.Value), nil
	default:
		return "", fmt.Errorf("unknown scalar type")
	}
}

// Create a new RegoDocument
func NewRegoDocument(path ...string) RegoDocument {
	return RegoDocument{Path: path}
}

// Call the given document as a function
func (r RegoDocument) AsFunction() RegoFunction {
	return RegoFunction{Path: r}
}

// Add a scalar argument to the function call
func (r RegoFunction) Arg(value interface{}) RegoFunction {
	s := RegoScalar{Value: value}
	r.Args = append(r.Args, AsRego(s))
	return r
}
