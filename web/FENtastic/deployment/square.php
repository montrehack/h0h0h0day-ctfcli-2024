<?php

class CipherSquareChallenge {
    private $grid;
    private $encryptedFlag;

    public function __construct() {
        $this->grid = array_fill(0, 9, array_fill(0, 9, ''));
        $this->populateGrid();
        $this->encryptedFlag = $this->encryptFlag();
    }

    private function populateGrid() {
        $symbols = array_merge(range('A', 'Z'), range(0, 9));
        shuffle($symbols);

        $symbolIndex = 0;
        for ($i = 0; $i < 9; $i++) {
            for ($j = 0; $j < 9; $j++) {
                if ($symbolIndex < count($symbols)) {
                    $this->grid[$i][$j] = $symbols[$symbolIndex];
                    $symbolIndex++;
                } else {
                    $this->grid[$i][$j] = $symbols[($i * $j + $i + $j) % count($symbols)];
                }
            }
        }
    }

    private function encryptFlag() {
        $flag = "15TH4TN0TTH3R1GHTF7AGQU3ST10NM4RK";
        $encrypted = "";

        for ($k = 0; $k < strlen($flag); $k++) {
            $char = $flag[$k];
            if (!ctype_alnum($char)) {
                $encrypted .= $char;
                continue;
            }

            $found = false;
            for ($i = 0; $i < 9; $i++) {
                for ($j = 0; $j < 9; $j++) {
                    if ($this->grid[$i][$j] == $char) {
                        $encrypted .= ($i + 1) . ($j + 1);
                        $found = true;
                        break;
                    }
                }
                if ($found) break;
            }
        }

        return $encrypted;
    }

    public function getChallengePage() {
        $html = "<h1>Crypto Grid Challenge</h1>";
        $html .= "<p>You've intercepted an encrypted message and a 9x9 grid. The encryption method involves translating characters to their grid positions.</p>";
        $html .= "<h2>Encrypted Flag:</h2>";
        $html .= "<p><strong>{$this->encryptedFlag}</strong></p>";
        $html .= "<h2>Grid Hints:</h2>";
        $html .= "<ol>
                    <li>The grid is filled to ensure all characters (A-Z, 0-9) appear at least once.</li>
                    <li>The placement uses a shuffled sequence combined with a mathematical pattern.</li>
                    <li>Decode the flag by understanding the grid's generation rule.</li>
                  </ol>";
        $html .= "<h2>Grid:</h2>";
        $html .= "<pre>";
        foreach ($this->grid as $row) {
            $html .= implode(" ", $row) . "\n";
        }
        $html .= "</pre>";
        $html .= "<p>Good luck, cryptographer!</p>";
        return $html;
    }
}

// Generate and display the challenge
$challenge = new CipherSquareChallenge();
echo $challenge->getChallengePage();

