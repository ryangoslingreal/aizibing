package aizibing;
import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

class GeneticSystem {
    boolean[][] genes = new boolean[10][10];
    Random rand = new Random(42);

    public void initialise() {
        for (int x = 0; x < 10; x++) {
            for (int y = 0; y < 10; y++) {
                genes[x][y] = rand.nextInt(2) == 0; // Randomly generate 0 or 1
            }
        }
        sortGenesByFitness();
    }

    // java provides nice function for us :D ... when sorting compared to fitness, we obviously have to call fitness (twice). should we cache gene's fitness WITH array? i.e pair them together... for now just use this
    public void sortGenesByFitness() {
        Arrays.sort(genes, (g1, g2) -> Float.compare(fitness(g2), fitness(g1))); // Sort in descending order
    }

    private boolean MINMAX_FITNESS = true; // true = maximise, false = minimise

    private float ELITE_PERCENT = 0.2f;
    private float KILL_PERCENT = 0.2f;
    private int ELITE_THRESHOLD = (int) (10 * ELITE_PERCENT); // 10 = population
    private int KILL_THRESHOLD = 10 - (int) (10 * KILL_PERCENT); // 10 - (10 - 20%)


    boolean[] crossover(boolean[] parent1, boolean[] parent2) {
        boolean[] child = new boolean[10];
        int crossoverPoint = rand.nextInt(10); // generate random split point

        // implement 'cross over more from fitter parent'?
        
        for (int i = 0; i < 10; i++) {
            child[i] = (i < crossoverPoint) ? parent1[i] : parent2[i];
        }

        return child;
    }


    public void step() {
        // loop thru genes, sort by fitness?

        boolean[][] newGenes = new boolean[10][10];

        // elitism - ignore top X%
        for (int i = 0; i < ELITE_THRESHOLD; i++) {
            newGenes[i] = genes[i];
        }

        // crossover & mutation 
        for (int i = ELITE_THRESHOLD; i < KILL_THRESHOLD; i++) {
            // random parent selection. kinda bad since we want higher fitness = higher chance of being parent. Alternatives : Tournament O(1) and roulette wheel O(n)
            int p1 = rand.nextInt(10); 
            int p2 = rand.nextInt(10); 
            
            newGenes[i] = crossover(genes[p1], genes[p2]);
            // add mutation ?
        }

        for (int i = KILL_THRESHOLD; i < 10; i++) { // kill introduces bad genes intentionally, however inhibits genes getting 'stuck'? (run code with and without kill to see)
            for (int y = 0; y < 10; y++) {
                newGenes[i][y] = rand.nextInt(2) == 0; // randomly generate 0 or 1
            }
        }


        //for (int i = 0; i < 10; i++) {
            // Implement logic for new gene creation based on the fitness
        //}

        genes = newGenes;
        sortGenesByFitness(); // sort at end of each step, rather than start. otherwise final step leaves genes unsorteds
    }

    public void outputGene(int n) {
        for (int y = 0; y < 10; y++) {
            System.out.print(genes[n][y] ? 1 : 0);
        }
        //System.out.println();
    }

    // fitness function = sum all 'true'
    public float fitness(boolean[] gene) {
        int sum = 0;
        for (int i = 0; i < 10; i++) {
            if (MINMAX_FITNESS ? gene[i] : !gene[i]) { // if we want to maximise, gene[i] must be true. otherwise, minimise > gene[i] must be false.
                sum++;
            }
        }
        return sum;
    }
}

public class Main {
    public static void clear() {
        System.out.print("\033[H\033[2J");  
        System.out.flush();
    }
    public static void main(String[] args) {
        clear(); // just cuz vscode makes some ugly outputs

        GeneticSystem GS = new GeneticSystem();
        GS.initialise();

        /*for (int i = 0; i < 0; i++) {
            GS.step();
        }*/

        Scanner s = new Scanner(System.in);

        int gen = 0;

        do {
            clear();
            System.out.println("Generation: " + ++gen);
        
            GS.step(); // Advance to the next generation
        
            for (int i = 0; i < 10; i++) {
                GS.outputGene(i);
                System.out.println("    " + GS.fitness(GS.genes[i]));
            }
            s.nextLine(); // Wait for user input
        }
        while (s.hasNextLine());
        
        /*GS.outputGene(0);
        System.out.println(GS.fitness(GS.genes[0]));

        GS.outputGene(9);
        System.out.println(GS.fitness(GS.genes[9]));*/
    }
}
