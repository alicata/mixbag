
#define PI  3.14159265359
#define EPS 0.01


float sharpen(in float d, in float w)
{ 
    float e = 1. / min(iResolution.y , iResolution.x);
    return 1. - smoothstep(-e, e, d - w);
}

float mkDisk(in vec2 p, in vec2 c, in float r, in float thickness)
{
    float resDisk = clamp(length(p - c) - r, 0., 1.);
    return sharpen(resDisk, EPS * thickness);
}

float mkCircle(in vec2 p, in vec2 c, in float r, in float thickness)
{
    float resCircle =  abs(r - length(p - c));
    
    return sharpen(resCircle, EPS * thickness);
    
}

float mkLine(in vec2 p, in vec2 a, in vec2 b, in float thickness)
{
    vec2 pa = p - a, ba = b - a;
	float h = clamp(dot(pa,ba) / dot(ba,ba), 0., 1.);	
	float lineResult = length(pa - ba * h);
    
    return sharpen(lineResult, EPS * thickness);
}

vec2 rotate(in vec2 p, in float t)
{
    t = t * 2. * PI;
    return vec2(p.x * cos(t) - p.y * sin(t), p.y * cos(t) + p.x * sin(t));
}

vec2 mkDirection(in float angle, in float len)
{
    vec2  unitVector = vec2(0,1);
    return  rotate(unitVector,angle) * len;   
}

float test(vec2 uv)
{    
    
    
    vec2 cxy = vec2(0);
    float radius = 0.79;
    float circThickness = 5.13;
    float resCircle = mkCircle(uv,cxy, radius, circThickness);
    
   
    vec2  unitVector = vec2(0,1);
    vec2 pStart = vec2(0.0, 0.0);
    vec2 vecLine = mkDirection(0.125, 0.5);
    
    
    float resLine = mkLine(uv, pStart, vecLine, 1.5);
    for (float k = 0.0; k < 10.0; k += 1.3) 
    {
        resLine += mkLine(uv, vec2(k/10.0,0), vecLine + vec2(k/10.0, 0), 1.5);
        resLine = min(resLine, 1.0);
    }
    
    return max( resLine, resCircle );
}

void main(void)
{
	vec2 uv = (gl_FragCoord.xy / iResolution.xy * 2. - 1.);
    uv.x *= iResolution.x / iResolution.y;
    vec3 col = vec3(0);
    
 
    col += test(uv);
 
    
	gl_FragColor = vec4(col, 1);
}
