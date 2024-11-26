# from fastapi import FastAPI, Body, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from typing import List, Dict

# app = FastAPI()

# # Add CORS middleware to allow requests from the React app (running on localhost:3000)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000"],  # Allow React app running on localhost:3000
#     allow_credentials=True,
#     allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
#     allow_headers=["*"],  # Allow all headers
# )

# # Root endpoint to verify if the server is up
# @app.get('/')
# def read_root():
#     return {'Ping': 'Pong'}

# # Endpoint for parsing pipeline
# @app.post('/pipelines/parse')
# def parse_pipeline(pipeline: dict = Body(...)):
#     """
#     Parse the pipeline to calculate the number of nodes and edges,
#     and check if the graph is a Directed Acyclic Graph (DAG).
#     """

#     # Extract nodes and edges from the input pipeline
#     nodes = pipeline.get("nodes", [])
#     edges = pipeline.get("edges", [])

#     # Validate input types
#     if not isinstance(nodes, list) or not isinstance(edges, list):
#         raise HTTPException(
#             status_code=400,
#             detail="'nodes' and 'edges' must be lists."
#         )
    
#     # Ensure every node has an 'id'
#     if not all("id" in node for node in nodes):
#         raise HTTPException(
#             status_code=400,
#             detail="Each node must have an 'id'."
#         )
    
#     # Ensure every edge has 'from' and 'to' keys
#     if not all("from" in edge and "to" in edge for edge in edges):
#         raise HTTPException(
#             status_code=400,
#             detail="Each edge must have 'from' and 'to' keys."
#         )
    
#     # Ensure that all 'from' and 'to' node IDs are valid
#     node_ids = {node["id"] for node in nodes}
#     if not all(edge["from"] in node_ids and edge["to"] in node_ids for edge in edges):
#         raise HTTPException(
#             status_code=400,
#             detail="Edges reference invalid node IDs."
#         )

#     num_nodes = len(nodes)
#     num_edges = len(edges)

#     # Check if the graph is a Directed Acyclic Graph (DAG)
#     def is_dag(nodes, edges):
#         """
#         Function to check whether the graph is a Directed Acyclic Graph (DAG)
#         using Depth-First Search (DFS) for cycle detection.
#         """
#         # Create adjacency list from the nodes and edges
#         adj_list = {node['id']: [] for node in nodes}
#         for edge in edges:
#             adj_list[edge['from']].append(edge['to'])

#         # Helper function for DFS and cycle detection
#         def dfs(node, visited, rec_stack):
#             visited.add(node)
#             rec_stack.add(node)
#             for neighbor in adj_list[node]:
#                 if neighbor not in visited:
#                     if not dfs(neighbor, visited, rec_stack):
#                         return False
#                 elif neighbor in rec_stack:
#                     return False
#             rec_stack.remove(node)
#             return True

#         # Initialize visited and recursion stack sets
#         visited, rec_stack = set(), set()
#         for node in adj_list:
#             if node not in visited:
#                 if not dfs(node, visited, rec_stack):
#                     return False
#         return True

#     is_graph_dag = is_dag(nodes, edges)

#     # Return the parsed results in a consistent format
#     return {
#         "num_nodes": num_nodes,
#         "num_edges": num_edges,
#         "is_dag": is_graph_dag
#     }

