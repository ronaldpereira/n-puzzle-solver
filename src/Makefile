test:
	python3 solver.py input/solution_1.txt -o output/solution_1/

	python3 solver.py input/solution_5.txt -o output/solution_5/

	python3 solver.py input/solution_8.txt -o output/solution_8/ -k 30

	# From here on, just a-star algorithm solves in an acceptable time

	python3 solver.py input/solution_9.txt -o output/solution_9/ -a

	python3 solver.py input/solution_10.txt -o output/solution_10/ -a

	python3 solver.py input/solution_15.txt -o output/solution_15/ -a

	python3 solver.py input/solution_20.txt -o output/solution_20/ -a

	python3 solver.py input/solution_25.txt -o output/solution_25/ -a

	python3 generator.py input/15_puzzle_solution_20.txt -n 4 -c 20
	python3 solver.py input/15_puzzle_solution_20.txt -o output/15_puzzle_solution20/ -a

	python3 generator.py input/15_puzzle_solution_20.txt -n 5 -c 20
	python3 solver.py input/15_puzzle_solution_20.txt -o output/15_puzzle_solution20/ -a

	python3 generator.py input/24_puzzle_solution_25.txt -n 6 -c 20
	python3 solver.py input/24_puzzle_solution_25.txt -o output/24_puzzle_solution25/ -a

	# This last three tests takes longer than the average even for the astar algorithm only

	python3 generator.py input/143_puzzle_solution_40.txt -n 12 -c 20
	python3 solver.py input/143_puzzle_solution_40.txt -o output/143_puzzle_solution40/ -a

	python3 solver.py input/solution_31.txt -o output/solution_31/ -a

