## Zero-Shot Prompting
Prompt:
```
Classify the text into neutral, negative or positive. 

Text: I think the vacation is okay.
Sentiment:
```
Output:
```
Neutral
```

## Few-Shot Prompting
Prompt:
```
A "whatpu" is a small, furry animal native to Tanzania. An example of a sentence that uses the word whatpu is:
We were traveling in Africa and we saw these very cute whatpus.
 
To do a "farduddle" means to jump up and down really fast. An example of a sentence that uses the word farduddle is:
```
Output:
```
When we won the game, we all started to farduddle in celebration.
```

Tips for Few-Shot Prompting
- "the **label space** and the **distribution of the input text** specified by the demonstrations are both important (regardless of whether the labels are correct for individual inputs)"
- the **format** you use also plays a key role in performance, even if you just use random labels, this is much better than no labels at all.
- additional results show that **selecting random labels from a true distribution of labels** (instead of a uniform distribution) also helps.

## Chain-of-Thought Prompting
Prompt:
```
I went to the market and bought 10 apples. I gave 2 apples to the neighbor and 2 to the repairman. I then went and bought 5 more apples and ate 1. How many apples did I remain with?

Let's think step by step.
```
Output:
```
First, you started with 10 apples.
You gave away 2 apples to the neighbor and 2 to the repairman, so you had 6 apples left.
Then you bought 5 more apples, so now you had 11 apples.
Finally, you ate 1 apple, so you would remain with 10 apples.
```

## Meta Prompting
### Example:
**Problem Statement:**
- **Problem:** [question to be answered]

**Solution Structure:**
1. Begin the response with "Let’s think step by step."
2. Follow with the reasoning steps, ensuring the solution process is broken down clearly and logically.
3. End the solution with the final answer encapsulated in a LaTeX-formatted box, `\boxed{...}`, for clarity and emphasis.
4. Finally, state "The answer is [final answer to the problem].", with the final answer presented in LaTeX notation.

## Generate Knowledge Prompting
First Generate the knowledge that the LLM lacks:
```
Input: Greece is larger than mexico.
Knowledge: Greece is approximately 131,957 sq km, while Mexico is approximately 1,964,375 sq km, making Mexico 1,389% larger than Greece.

Input: Glasses always fog up.
Knowledge: Condensation occurs on eyeglass lenses when water vapor from your sweat, breath, and ambient humidity lands on a cold surface, cools, and then changes into tiny drops of liquid, forming a film that you see as fog. Your lenses will be relatively cool compared to your breath, especially when the outside air is cold.

Input: A fish is capable of thinking.
Knowledge: Fish are more intelligent than they appear. In many areas, such as memory, their cognitive powers match or exceed those of ’higher’ vertebrates including non-human primates. Fish’s long-term memories help them keep track of complex social relationships.

Input: A common effect of smoking lots of cigarettes in one’s lifetime is a higher than normal chance of getting lung cancer.
Knowledge: Those who consistently averaged less than one cigarette per day over their lifetime had nine times the risk of dying from lung cancer than never smokers. Among people who smoked between one and 10 cigarettes per day, the risk of dying from lung cancer was nearly 12 times higher than that of never smokers.

Input: A rock is the same size as a pebble.
Knowledge: A pebble is a clast of rock with a particle size of 4 to 64 millimetres based on the Udden-Wentworth scale of sedimentology. Pebbles are generally considered larger than granules (2 to 4 millimetres diameter) and smaller than cobbles (64 to 256 millimetres diameter).

Input: Part of golf is trying to get a higher point total than others.
Knowledge:
```
Generated Knowledge:
```
The objective of golf is to play a set of holes in the least number of strokes. A round of golf typically consists of 18 holes. Each hole is played once in the round on a standard golf course. Each stroke is counted as one point, and the total number of strokes is used to determine the winner of the game.
```

Then integrate the knowledge into the prompt:
```
Question: Part of golf is trying to get a higher point total than others. Yes or No?

Knowledge: The objective of golf is to play a set of holes in the least number of strokes. A round of golf typically consists of 18 holes. Each hole is played once in the round on a standard golf course. Each stroke is counted as one point, and the total number of strokes is used to determine the winner of the game.

Explain and Answer: 
```
Answer:
```
No, the objective of golf is not to get a higher point total than others. Rather, the objective is to play a set of holes in the least number of strokes. The total number of strokes is used to determine the winner of the game, not the total number of points.
```

## Prompt Chaining
Break the prompts into several sub-tasks, after finish one sub-task, integrate the result into the next prompt until finish the prompt.

## Tree of Thoughts
ToT maintains a tree of thoughts, where thoughts represent coherent language sequences that serve as intermediate steps toward solving a problem.

## Automatic Prompt Engineering
## Active Prompting
First generate several Q and A pairs, then score the pairs by some uncertainty measurement, finally humans are to annotate the pairs that are the most uncertain.

## Directional Stimulus Prompting
Use a RL-trained LM to generate stimulus (hint) given a prompt

## Promgram Aided Language Models
Convert the intermeidate thoughts into executable python programs then use the cli to excute the generate programs/codes.

## ReAct
Ideas: interact with external tools to retrieve additional information that leads to more reliable and factual responses.

Example:
```
Question What is the elevation range for the area that the eastern sector of the
Colorado orogeny extends into?
Thought 1 I need to search Colorado orogeny, find the area that the eastern sector
of the Colorado orogeny extends into, then find the elevation range of the
area.
Action 1 Search[Colorado orogeny]
Observation 1 The Colorado orogeny was an episode of mountain building (an orogeny) in
Colorado and surrounding areas.
Thought 2 It does not mention the eastern sector. So I need to look up eastern
sector.
Action 2 Lookup[eastern sector]
Observation 2 (Result 1 / 1) The eastern sector extends into the High Plains and is called
the Central Plains orogeny.
Thought 3 The eastern sector of Colorado orogeny extends into the High Plains. So I
need to search High Plains and find its elevation range.
Action 3 Search[High Plains]
Observation 3 High Plains refers to one of two distinct land regions
Thought 4 I need to instead search High Plains (United States).
Action 4 Search[High Plains (United States)]
Observation 4 The High Plains are a subregion of the Great Plains. From east to west, the
High Plains rise in elevation from around 1,800 to 7,000 ft (550 to 2,130
m).[3]
Thought 5 High Plains rise in elevation from around 1,800 to 7,000 ft, so the answer
is 1,800 to 7,000 ft.
Action 5 Finish[1,800 to 7,000 ft]
...
```

## Reflexion
Compared to "ReAct", an LLM evaluator is added to evaluate the trajactory, and save the rewards based on the evaluations. The self-reflection model makes use of the reward signal, the current trajectory, and its persistent memory to output relection texts. Finally, the LLM uses this text to take the next action.

