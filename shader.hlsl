float result = 0;

for (int i = 0; i < nSides; i++)
{
    for (int j = 0; j < nCopies; j++)
    {
        float angle = (i /nSides) * sin(time * 2) * (3.14 * 2);
        float2 pos = center + (j / nCopies) * radius * float2(sin(1-angle), cos(1-angle));

        result += length(pos - uv) < size;
    }

}
color = result * float3(sin(time),cos(time),sin(90-time)+ 0.01);
return(result);