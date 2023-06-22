#version 330 core

layout (location=0) out vec4 fragColor;

in vec2 uv_1;
in vec3 normal;
in vec3 fragPos;

uniform sampler2D u_texture_1;

struct Light
{
    vec3 position;
    vec3 Ia;
    vec3 Id;
    vec3 Is;
};

uniform Light light;
uniform vec3 camPos;


void main()
{
    // Material properties
    vec3 materialKa = vec3(0.1, 0.1, 0.1);  // Ambient coefficient
    vec3 materialKd = vec3(0.8, 0.8, 0.8);  // Diffuse coefficient
    vec3 materialKs = vec3(0.5, 0.5, 0.5);  // Specular coefficient
    float materialShininess = 32.0;        // Shininess factor

    // Ambient component
    vec3 ambient = light.Ia * materialKa;

    // Diffuse component
    vec3 lightDir = normalize(light.position - fragPos);
    float diffuseFactor = max(dot(normal, lightDir), 0.0);
    vec3 diffuse = light.Id * materialKd * diffuseFactor;

    // Specular component
    vec3 viewDir = normalize(camPos - fragPos);
    vec3 reflectDir = reflect(-lightDir, normal);
    float specularFactor = pow(max(dot(viewDir, reflectDir), 0.0), materialShininess);
    vec3 specular = light.Is * materialKs * specularFactor;

    // Final color calculation
    vec3 color = texture(u_texture_1, uv_1).rgb;
    vec3 finalColor = color * (ambient + diffuse) + specular;
    fragColor = vec4(finalColor, 1.0);
}