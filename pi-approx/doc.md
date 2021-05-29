 - pi.py generates a csv kind of output
 - analyse.py gets the input a csv file whose average we should calculate

Initial knowlege:
	- random() generates random floating point numbers in [0.0,1.0)
	- uniform(0, 1) generates random floating point numbers in [0,0,1.0]
	- source: 'https://stackoverflow.com/questions/30030659/in-python-what-is-the-difference-between-random-uniform-and-random-random'

Hypothesis:
	- uniform should generate more accurate approximation for pi
	- since it includes one more number
	- But will that make a real difference
	- lets see

After analysis
	- My hypothesis was wrong :(
	- The difference between random and uniform is not appreciable enough
	- for details check analyse.ipynb
