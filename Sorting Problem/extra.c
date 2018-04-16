
int rets = remove(char filename[]){
    
    int ret;
    ret = rets = remove(filename);
    
    if(ret == 0)
    {
        printf("File %s deleted successfully", filename);
    }
    else
    {
        printf("Error: unable to delete the file %s", filename);
    }
    
    return(0);
    
}