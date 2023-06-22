#version 330 core

layout (location=0) in vec2 in_texcoord_0;
layout (location=1) in vec3 in_normal;
layout (location=2) in vec3 in_position;

uniform mat4 m_matrix;
uniform mat4 v_matrix;
uniform mat4 p_matrix;

out vec2 uv_1;
out vec3 normal;
out vec3 fragPos;

void main(){
    fragPos = vec3(m_matrix * vec4(in_position, 1.0));
    normal = mat3(transpose(inverse(m_matrix))) * normalize(in_normal);
    gl_Position = p_matrix * v_matrix * m_matrix * vec4(in_position, 1.0);
    uv_1 = in_texcoord_0;
}