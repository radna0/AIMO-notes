from newclid import GeometricSolverBuilder, GeometricSolver

solver_builder = GeometricSolverBuilder(2024)
solver_builder.load_problem_from_txt(
    "a b c = triangle a b c; h = orthocenter a b c; g1 g2 g3 g = centroid g1 g2 g3 g a b c; o = circle a b c ? coll h g o"
)

# We now obtain the GeometricSolver with the build method
solver: GeometricSolver = solver_builder.build()

# And run the GeometricSolver
success = solver.run()

if success:
    print("Successfuly solved the problem!")
else:
    print("Failed to solve the problem...")

print(f"Run infos {solver.run_infos}")
