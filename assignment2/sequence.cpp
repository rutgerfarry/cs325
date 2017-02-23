/* Miles A. Curry (currymi) - Rhea Mae Edwards (edwardrh)
 * CS325-001 - Winter 2017
 *
 * Implementation Assignment 2
 */

#ifndef INCLUDES
#define INCLUDES
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <fcntl.h>
#include <time.h>
#endif

/* C++ Headers */
#ifndef C2HEADERS
#define C2HEADERS
#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#endif

#ifndef DEFINES
#define DEFINES
#define COMMA 44
#define SPACE 32
#define NEWLINE 10
#endif

/* Sequence Alignment Solution */
class seqAli {

private:
	vector < vector <int> > DP;
	vector <int> outCost;


public:
	vector <string> input;
	vector <string> output;
	vector <string> cost;

	vector <string> get_input() {return input;}
	vector <string> get_output() {return output;}

	/* Creates our edit distance solution that should be output to
	 * imp2output.txt */

	void printValues(vector <string> &v){
		int i, j;
		
		for(i = 0; i < v.size(); i+=2){
			cout << v[i] << endl << v[i+1] << endl;
		}

		return;
	}

	void printValues(vector <string> &v, const char *fname){
		int i, j;
		ofstream file;
		file.open(fname);
		
		for(i = 0; i < v.size(); i++){
			file << v[i] << " ";
		}
		return;
	}

	void printValues(vector <string> &v, const char *fname, vector<int> &cost){
		int i, j;
		ofstream file;
		file.open(fname);
		
		for(i = 0; i < v.size(); i+=2){
			file << v[i] << "," << v[i] << "*" << cost[i] << endl;
		}
		return;
	}

	void printValues(vector< vector<int> > &v){
		int i, j;
		
		for(i = 0; i < v.size(); i++){
			for(j = 0; j < v[i].size(); j++){
				cout << fixed <<v[i][j] << " ";
			}
			cout << endl;
		}
		return;
	}

	void printValues(vector< vector<double> > &v){
		int i, j;
		
		for(i = 0; i < v.size(); i++){
			for(j = 0; j < v[i].size(); j++){
				cout << fixed <<v[i][j] << " ";
			}
			cout << endl;
		}
		return;
	}


	int getCostFile(FILE *fp){
		int i;
		char line[500];
		char value1[500];

		while(fgets(line, sizeof(line), fp)){
			cost.push_back(line); // Add a new row to our vector
		}

		return 1;
	}


	int getContents(FILE *fp){
		char line[256];
		char value1[10000], value2[10000];

		/* 1 == First Value 2 == end value */
		int flag, j; 
		int k=0;

		//TODO: Add a check to see if the file exists or not

		while(fgets(line, sizeof(line), fp)){
			memset(&value1, 0, sizeof(value1));  
			memset(&value2, 0, sizeof(value2));  
			flag = 1;
			j = 0;
			
			for(int i = 0; line[i] != NEWLINE; i++){
				if(line[i] == COMMA){
					flag = 2;
					continue;
				}
				else if(flag == 1 ){
					value1[i] = line[i];
				}
				else if(flag == 2){
					value2[j++] = line[i];
				}
			}

			if(debug_value > 0){
				cout << "V1 = " << value1 << endl
				<< " V2 = " << value2 
				<< endl;
			}

			input.push_back(value1); // Add a new row to our vector
			input.push_back(value2); // Add a new row to our vector
			++k;
		}

		return 1;
	}

void solution() { 
	int i, j, line;


	if(cost.size() == false){
		cout << "NO Cost file inputed! Please input a cost file first! Thanks!\n" 		 << endl;
		exit(EXIT_FAILURE);
	}
		
	/* For each two lines input do: */
	for(line = 0; line < input.size(); line += 2){
		/* i = Value 1, i+1 = value 2 */	
		/* Clear DP each time we run the section below */
		DP.clear();
		

		int line1, line2;
		line1 = input[line].size();
		line2 = input[line+1].size();
	
		DP.resize(line1); //Reserve room for our first value


		/* Fill the height of our coloumns */
		for(i = 0; i < line1; i++){
			DP[i].resize(line2); // Reserve room for our rows
			DP[i][0] = i;
			for(j = 0; j < line2; j++){
				DP[0][j] = j;
			}
		}
		
		if(debug_value > 0){
			printValues(DP);
		}
		if(debug_value > 1){
			cout << " dp.size() = "    << DP.size() << endl;
			cout << " dp[1].size() = " << DP[1].size() << endl;
			cout << " input[line].size() = "    << input[line].size() << endl;
			cout << " input[line+1].size() = " << input[line+1].size() << endl;
		}


		/* For i=0 to m: D(i, 0) = i
		 * For j=1 to n: D(0, j) = j
		 * For each i = 1...m
		 *	For each j = 1..n
		 *		d(i,j) = min( D(i-1,j) + 1, Deletion
		 *			      D(i,j-1) + 1, Insertion
		 *			      D(i-1,j-1) + diff(si, tj) ) align
		 * Return D(m,n)
		 */

		int deletion, insertion, align;

	 	for(i = 1; i < DP.size(); i++){
			for(j = 1; j < DP[i].size(); j++){
				deletion  = DP[i][j-1] + 1;
				insertion = DP[i-2][j] + 1;
				align     = DP[i-1][j-1] + diff();
					
				if(deletion > 


			}	
		}
	
		





	}
}
 
};

