package aizibing;
import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

class GeneticSystem {
    public int GENE_POPULATION = 10; // could just add a getter and make these private but thats ugly
    public int GENE_LENGTH = 10;

    boolean[][] genes = new boolean[GENE_POPULATION][GENE_LENGTH];
    Random rand = new Random(); // set seed here!

    private boolean MINMAX_FITNESS = true; // true = maximise, false = minimise

    private float ELITE_PERCENT = 0.2f;
    private float KILL_PERCENT = 0.2f; //0.2f; // set to 0 to disable kill .. 
    private int ELITE_THRESHOLD = (int) (GENE_POPULATION * ELITE_PERCENT); // 10 = population
    private int KILL_THRESHOLD = GENE_POPULATION - (int) (GENE_POPULATION * KILL_PERCENT); // 10 - (10 - 20%)    - one thing to note, maybe dont kill & renoise every gen? 

    // initialise maybe return seed used?
    public long initialise() {
        long seed = rand.nextLong();
        rand.setSeed(seed);

        for (int x = 0; x < GENE_POPULATION; x++) {
            for (int y = 0; y < GENE_LENGTH; y++) {
                genes[x][y] = rand.nextInt(2) == 0; // randomly generate true or false
            }
        }
        
        sortGenesByFitness(); // needs to be sorted before worked on
        return seed;
    }

    // java provides nice function for us :D ... when sorting compared to fitness, we obviously have to call fitness (twice). should we cache gene's fitness WITH array? i.e pair them together... for now just use this
    public void sortGenesByFitness() {
        Arrays.sort(genes, (g1, g2) -> Float.compare(fitness(g2), fitness(g1))); // Sort in descending order
    }

    boolean[] crossover(boolean[] parent1, boolean[] parent2) {
        boolean[] child = new boolean[GENE_LENGTH];
        int crossoverPoint = rand.nextInt(GENE_LENGTH); // generate random split point

        // implement 'cross over more from fitter parent'?
        
        for (int i = 0; i < GENE_LENGTH; i++) {
            child[i] = (i < crossoverPoint) ? parent1[i] : parent2[i];
        }

        return child;
    }


    public void step() {
        // loop thru genes, sort by fitness?

        boolean[][] newGenes = new boolean[GENE_POPULATION][GENE_LENGTH];

        // elitism - ignore top X%
        for (int i = 0; i < ELITE_THRESHOLD; i++) {
            newGenes[i] = genes[i];
        }

        // crossover & mutation 
        for (int i = ELITE_THRESHOLD; i < KILL_THRESHOLD; i++) {
            // random parent selection. kinda bad since we want higher fitness = higher chance of being parent. Alternatives : Tournament O(1) and roulette wheel O(n)
            int p1 = rand.nextInt(GENE_POPULATION); 
            int p2 = rand.nextInt(GENE_POPULATION); // randomly select parent from population
            
            newGenes[i] = crossover(genes[p1], genes[p2]);
            // add mutation ?
        }

        for (int i = KILL_THRESHOLD; i < GENE_POPULATION; i++) { // kill introduces bad genes intentionally, however inhibits genes getting 'stuck'? (run code with and without kill to see)
            for (int y = 0; y < GENE_LENGTH; y++) {
                newGenes[i][y] = rand.nextInt(2) == 0; // randomly generate 0 or 1
            }
        }


        genes = newGenes;
        sortGenesByFitness(); // sort at end of each step, rather than start. otherwise final step leaves genes unsorteds
    }

    public void outputGene(int n) {
        for (int y = 0; y < GENE_LENGTH; y++) {
            System.out.print(genes[n][y] ? 1 : 0);
        }
        //System.out.println();
    }

    // fitness function = sum all 'true'
    public float fitness(boolean[] gene) {
        int sum = 0;
        for (int i = 0; i < GENE_LENGTH; i++) {
            if (i == 3 && gene[i]) sum-=5;
            if (MINMAX_FITNESS ? gene[i] : !gene[i]) { // if we want to maximise, gene[i] must be true. otherwise, minimise means gene[i] must be false.
                sum++;
            }
        }
        return sum;
    }
}

public class Main {
    public static void main(String[] args) {
        GeneticSystem GS = new GeneticSystem();

        long seed = GS.initialise();
        System.out.println("Seed: " + seed);

        Scanner s = new Scanner(System.in);
        int gen = 0; 

        do {
            System.out.println("Generation: " + gen++);
        
            for (int i = 0; i < GS.GENE_POPULATION; i++) {
                System.out.print(i + 1 + ": ");
                GS.outputGene(i);
                System.out.println("    " + GS.fitness(GS.genes[i]));
            }
            System.out.println();
            
            GS.step(); // step to next gen, put at end to show gen 0
            s.nextLine(); // wait for next input
        }
        while (s.hasNextLine());
        s.close();
    }
}

/*

how can we prevent 80% of genes getting max fitness, then due to swapover retrace back to dumb? 
^ kill obviously affects this

then again, does it really matter ? for larger populations it'll be unlikely anyway

*/