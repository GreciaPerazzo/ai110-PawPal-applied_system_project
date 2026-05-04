# Model Card — PawPal+ Applied AI System
It is a model specification for the PawPal+ Automated Intelligence System.

### Artificial Intelligence Interaction
Throughout the project, I used Claude (Anthropic) as my project assistant.

**Trait of Value:** Used Claude to determine the location of the AI function in app.py; it was indented within an else statement that caused it to vanish once tasks were added. This helped a lot through  debugging.

**Trait Lacking Value:** Originally, Claude suggested gemini-1.5-flash as a model name; however, because it was out of date, it caused a 404 error. Therefore, I had to find and change it to gemma-3-27b-it.

### AI Limitations and Biases
- The AI presumes every pet has an equivalent amount of care needs based upon either the species or breed; however, these assumptions may not accurately describe each animal's unique health status.
- The breed-specific recommendations provided by Gemini are based solely upon written information and may not accurately apply to every pet on an individual level.
- Currently, the PawPal+ system can only perform in the English language; therefore, it cannot assist pet owners that do not speak English.
- AI output may differ from one execution to another, the same input can lead to different recommendations from AI.

## Risks of Misuse
- People  have the ability to completely rely on AI generated care plans rather than consulting a veterinarian for any medical related tasks such as medication scheduling.
- A notice in the app states that the AI suggestions provided within the application are not to be considered as providing professional veterinary advice.

## What I Learned In My Testing
- AI performed really well with little to no task information; it filled in the breed specific knowledge on its own.
- In addition to fixing the quota issue when I switched from gemini-2.0-flash to gemma-3-27b-it, it also produced responses that were much warmer than previously seen responses.
- I ran the evaluation script from the AI tests, and out of a possible 3/3 AI tests, all passed, which was much better than I had predicted.

---

## Testing Results
- 5/5 pytest unit tests cover core scheduling logic
- 3/3 AI evaluation tests passed using `evaluate.py`
- Logging captures all API calls and errors for transparency