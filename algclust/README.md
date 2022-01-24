# algclust

Construction of clustering algorithms

# docker instructions

```sh
   docker build -f Dockerfile -t python_local .
   docker run --rm --name clusters -p 8888:8888 -v $(pwd)/:/project -d python_local:latest
   docker logs clusters
   docker exec -it clusters bash
```
