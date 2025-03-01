categorize_prompt = """
Problem: "Three airline companies operate flights from Dodola island. Each company has a different schedule of departures. The first company departs every 100 days, the second every 120 days and the third every 150 days. What is the greatest positive integer $d$ for which it is true that there will be $d$ consecutive days without a flight from Dodola island, regardless of the departure times of the various airlines?"

You are provided with a mathematical problem. Your task is to analyze the problem and determine which single category it belongs to from the following list:
- Algebra
- Geometry
- Combinatorics
- Number Theory

**Instructions:**

1. **Categorization Only:**  
   - Your sole responsibility is to categorize the problem. Do **not** attempt to solve it or provide any solution steps.
  
2. **Analysis Focus:**  
   - Read the problem carefully and identify key elements (e.g., variables, equations, figures, counting arguments, or numerical properties) that indicate the relevant category.
  
3. **Output Format:**  
   - Provide your answer by outputting only the category name, enclosed in a box. Use the exact format:  
     `\boxed{<Category>}`
   - Replace `<Category>` with one of the following: Algebra, Geometry, Combinatorics, or Number Theory.

4. **No Additional Information:**  
   - Do not include any explanations, justifications, or extra text beyond the boxed answer.
"""
