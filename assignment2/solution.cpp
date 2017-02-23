/* Miles A. Curry (currymi) - Rhea Mae Edwards (edwardrh)
 * CS325-001 - Winter 2017
 *
 * Implementation Assignment 2 - Sequence Alignment
 */

#include "header.h"
#include "sequence.cpp"

FILE * cost;
FILE * input;
FILE * output;

void help(){
	printf("\t -v: Turn on Debuger text\n");
	printf("\t\t 1: debug output \n");
	printf("\t\t 2: we gonna blow your mind with debug output\n");
	printf("\t\t 3: we gonna blow your mind with debug output\n");
	printf("\t -t [i] - Run test cases i\n");
	printf("\t -h: Show this help message\n");
	exit(EXIT_SUCCESS);
}

int main(int argc, char **argv)
{
	int opt; 


	while((opt=getopt(argc, argv, "hv:")) != -1){
		switch(opt){
		case 'v':
			debug_value = atoi(optarg);
			break;
		case 'h':
			help();
			break;
		}
	}

	cost   = fopen("imp2cost.txt",     "r");
	if(cost == NULL){
		fprintf(stderr, "ERROR: No imp2cost.txt File found \n");
		fprintf(stderr, "ERROR: EXITING\n");
		exit(EXIT_FAILURE);
	}
	input  = fopen("imp2input.txt",    "r");
	if(input == NULL){
		fprintf(stderr, "ERROR: No imp2out.txt file found \n");
		fprintf(stderr, "ERROR: EXITING\n");
		exit(EXIT_FAILURE);
	}
	output = fopen("imp2out.our.txt",  "w");
	if(output == NULL){
		fprintf(stderr, "ERROR: No imp2.txt file found \n");
		fprintf(stderr, "ERROR: EXITING\n");
		exit(EXIT_FAILURE);
	}


	/* Solution */	
	seqAli test;
	test.getContents(input);
	test.getCostFile(cost);
	test.solution();
	test.printValues(test.cost);



	return 1;
}

