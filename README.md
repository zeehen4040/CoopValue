# CoopValue: Revealing LLM Value Preferences Through Multi-Agent Cooperation

CoopValue is a dataset designed to study value preferences of Large Language Models (LLMs) in multi-agent cooperative settings under conflict. It enables researchers to analyze how LLMs prioritize different values when faced with trade-offs that cannot be simultaneously satisfied.

---

## Dataset Structure

The dataset contains a total of 1,778 instances. Each instance contains:

```json
{
  "Scenario": "A textual description of the multi-agent situation.",
  "Cooperation type": "Type of interaction between agents (Reciprocal, Coopetitive, or Altruistic).",
  "Value 1": "The Schwartz value primarily associated with the first agent.",
  "Value 2": "The Schwartz value primarily associated with the second agent.",
  "Conflict Rationale": "Explanation of why the agents' objectives are in conflict.",
  "Cooperation Rationale": "Explanation of why the interaction is categorized under the specified cooperation type."
}
