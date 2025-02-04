# 🧬 aizibing

simple **genetic algorithm** demo to develop our understanding
used for reference & feasibility

step through each generation and watch genes evolve!


## 📜 genetic system demo
📌 genetic sequence represented by 1's and 0's `(true and false)` 

📌 `fitness function` = sum of 1s in gene

## 🚀 features
✅ implements basic algorithms such as crossover

✅ added **KILL THRESHOLD** - basically 'regenerate' least fit

✅ choose to minimise or maximise fitness function

## 📝 to-do 
- improve crossover - *'fittest parent first'*.. yes please!
- implement mutation
- implement selection methods: tournament / roulette wheel selection 
- may need to cache fitness , use a pair system ?
- allow hyperparameters to customise system *(i.e add checks in GeneticSystem->Step, for example, include kill?)*
- create hyperparam class, where constants are accessed
