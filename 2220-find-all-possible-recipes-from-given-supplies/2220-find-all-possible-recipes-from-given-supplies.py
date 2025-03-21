from collections import defaultdict, deque
from typing import List

class Solution:
    def findAllRecipes(
        self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]
    ) -> List[str]:
        # Create a graph to map each ingredient to the recipes that require it
        graph = defaultdict(list)
      
        # Dictionary to keep track of the number of pending ingredients for each recipe
        incoming_edges = defaultdict(int)
      
        # Build the graph and update the incoming edges count for each recipe
        for recipe, required_ingredients in zip(recipes, ingredients):
            for ingredient in required_ingredients:
                graph[ingredient].append(recipe)
            incoming_edges[recipe] += len(required_ingredients)
      
        # Initialize a queue with the available supplies (ingredients)
        queue = deque(supplies)
      
        # List to store the possible recipes we can cook
        available_recipes = []
      
        # Process the queue until it's empty
        while queue:
            # Go through the current size of the queue (ingredients available at this level)
            for _ in range(len(queue)):
                ingredient = queue.popleft()
                # Check each recipe that can be made with the current ingredient
                for recipe in graph[ingredient]:
                    # Decrease the count of pending ingredients for the current recipe
                    incoming_edges[recipe] -= 1
                    # If all ingredients for the recipe are available, add to the list
                    if incoming_edges[recipe] == 0:
                        available_recipes.append(recipe)
                        # Add the newly available recipe to the queue
                        queue.append(recipe)
      
        # Return the list of recipes we can cook with the available supplies
        return available_recipes