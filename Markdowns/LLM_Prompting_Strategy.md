# LLM Prompting Strategy for HVAC Electronics Course

## Selected LLMs
1. GPT-4
2. Claude
3. Gemini

## Prompting Techniques by Output Type

### 1. Course Outline Generation

#### Zero-Shot Prompt Template
```
Generate a detailed course outline for "Introduction to Electronics in HVAC" with the following structure:
- Main topics (5-6)
- Subtopics for each main topic (2-3 per topic)
- Specific learning objectives for each subtopic (3-4 per subtopic)
Focus on practical applications and industry standards.
```

#### Few-Shot Prompt Template
```
Here's an example of a well-structured course outline:

Topic: Basic Electronics
Subtopics:
A. Circuit Components
   Learning Objectives:
   - Identify basic circuit elements
   - Explain component functions
   - Measure electrical values

Please create a similar structure for "Introduction to Electronics in HVAC" covering:
[Rest of instructions...]
```

### 2. Slide Content Generation

#### Chain-of-Thought Prompt Template
```
To create engaging slide content for [specific subtopic]:
1. First, identify the key concepts that need to be explained
2. Then, break down each concept into simple, digestible points
3. Finally, suggest relevant examples or applications in HVAC systems

Based on this approach, generate slide content for [specific subtopic]
```

### 3. Visual Learning Aids

#### Prompt Chain Template
```
Step 1: "What are the key visual elements needed to explain [concept]?"
Step 2: "Describe a clear, simple diagram that illustrates [concept]"
Step 3: "List the labels and annotations needed for the diagram"
Step 4: "Suggest animations or transitions that would help explain the concept"
```

## Tools for Prompt Optimization

1. OpenAI Playground
   - Used for: Testing different temperature settings and response formats
   - Benefits: Real-time feedback, easy prompt iteration

2. PromptPerfect
   - Used for: Enhancing clarity and reducing ambiguity
   - Benefits: Automated suggestions for improvement

3. AI Dungeon
   - Used for: Testing interactive learning scenarios
   - Benefits: Exploring conversational flow and engagement

## Evaluation Matrix for LLM Outputs

| Criteria | GPT-4 | Claude | Gemini |
|----------|-------|--------|---------|
| Technical Accuracy | | | |
| Clarity | | | |
| Engagement | | | |
| Consistency | | | |