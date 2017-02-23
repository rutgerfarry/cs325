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
#include <fcntl.h>
#include <errno.h>
#endif 

#ifndef C2HEADERS
#define C2HEADERS
/* C++ Headers */
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


int debug_value = 0;
using namespace std;

bool sortcol( const vector<double>& v1, const vector<double>& v2) {
	return v1[1] < v2[1];
}

/* distance formula from xoax.net/cpp/ref/cpp_example/incl/distance_points_plane/ */
double distance(double dx0, double dy0, double dx1, double dy1){
	return sqrt ((dx1 - dx0)*(dx1 - dx0) + (dy1 - dy0) * (dy1 - dy0));
}
/* Returns an open file descriptor */
int createFile(char const *name){
    int fd = -1;
    int flag = O_APPEND | O_RDWR | O_CREAT; // Open Flags
    int mode = S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH; // Permission Flags


    /* CREATE FILE NAME */
    fd = open(name, flag, mode);
    if(fd == -1){
	fprintf(stderr, "Could not create new file. Errno = %d\n", errno);
	perror("cannot create file");
	return -1;
    }

    /* CHECK j */
    if(-1 == access(name, F_OK)){
	printf("Error here\n");
	perror("ERROR:");
	return 0;
    }

    // Close FD
    return fd;
} 


