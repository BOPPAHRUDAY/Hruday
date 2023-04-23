#include<stdio.h>
#include<conio.h>
#define INFINITY 9999
#define MAX 10
void dij(int g[MAX][MAX],int n,int stnode);
int main()
{
    int g[MAX][MAX],i,j,n,u;
    printf("Enter number of vertices : ");
    scanf("%d",&n);
    printf("Enter the adjacency matrix\n");
    for(i=0;i<n;i++)
        for(j=0;j<n;j++)
            scanf("%d",&g[i][j]);
    printf("Enter the starting node : ");
    scanf("%d",&u);
    dij(g,n,u);
    return 0;
}
void dij(int g[MAX][MAX],int n,int stnode)
{
    int cost[MAX][MAX],dist[MAX],pred[MAX];
    int vis[MAX],count,mindist,nextnode,i,j;
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            if(g[i][j]==0)
                cost[i][j]=INFINITY;
            else
                cost[i][j]=g[i][j];
        }
    }
    for(i=0;i<n;i++)
    {
        dist[i]=cost[stnode][i];
        pred[i]=stnode;
        vis[i]=0;
    }   
    dist[stnode]=0;
    vis[stnode]=1;
    count=1;
    while(count<n-1)
    {
        mindist=INFINITY;
        for(i=0;i<n;i++)
        {
            if(dist[i]<mindist&&!vis[i])
            {
                mindist=dist[i];
                nextnode=i;
            }
        }
        vis[nextnode]=1;
        for(i=0;i<n;i++)
        {
            if(!vis[i])
            {
                if(mindist+cost[nextnode][i]<dist[i])
                {
                    dist[i]=mindist+cost[nextnode][i];
                    pred[i]=nextnode;
                }
            }
        }
        count++;
    }
    for(i=0;i<n;i++)
    {
        if(i!=stnode)
        {
            printf("Distance of node %d = %d\n",i,dist[i]);
            printf("Path = %d",i);
            j=i;
            do
            {
                j=pred[j];
                printf(" <- %d",j);
            }while(j!=stnode);
            printf("\n");
        }
    }
}
