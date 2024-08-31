% Crear una figura para graficar
figure;

% Graficar la señal x(t)
subplot(3, 1, 1);  % Crear la primera subgráfica
plot(t, x);        % Usar plot para señales continuas
title('Señal de entrada x(t)');
xlabel('t');
ylabel('x(t)');

% Graficar la señal h(t)
subplot(3, 1, 2);  % Crear la segunda subgráfica
plot(t, h);
title('Señal h(t)');
xlabel('t');
ylabel('h(t)');

% Graficar el resultado de la convolución
subplot(3, 1, 3);  % Crear la tercera subgráfica
plot(t, y);        % Nota: y puede ser más largo que t si no usas 'same'
title('Resultado de la convolución y(t)');
xlabel('t');
ylabel('y(t)');
