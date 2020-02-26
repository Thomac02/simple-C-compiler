int a[3][4] = {2, 4, 5 , 2, 4, 5, 2, 4, 5, 2, 4, 5};
int b;

int main(int argc, int argv){
	for(int i = 0; i < 3; i++){
        b += a[i][i- 2];
        b--;
    }
	return 0;
}	


