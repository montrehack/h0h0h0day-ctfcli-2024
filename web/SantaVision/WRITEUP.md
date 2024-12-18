# SantaVision

The arching theme of this challenge is to bypass locks enforced by the frontend.

## Part 1

1. Find the only video which is actually displaying something (a security footage of a house with a fireplace)
2. Notice the video seems to cut abruptly at the end, you can also notice some text starting on a parchment above the fireplace
3. Opening the video in a separate tab allows you to see the full video. 

Flag: `1_0n3_c4nn07`

## Part 2

One of the videos seems to be loading. Like all the videos, this one is muted.

- Add the `controls` attribute to the video allows you to unmute the video
- Or enable the `Mute` button for the same result
  
Flag: `2_7ru57_fr0n73nd`

## Part 3

One of the blurry videos has no sounds, but you can find there's a VTT file for subtitles 

- The quickest way to enable subtitles is to add the `controls` attribute to the `<video>` tag
- You can also open the sub,vtt file directly and sort the letters per timestamp.

Flag: `3_53cur17y_m345ur35`

## Final Flag
FLAG-0n3_c4nn07_7ru57_fr0n73nd_53cur17y_m345ur35
