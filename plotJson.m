data = jsondecode(fileread("Output.json"));
size = length(data);

X = zeros(size,1);
Y = zeros(size,1);
potential = zeros(size,1);
pixel = zeros(size,1);
sinus = zeros(size,1);

for i = 1:length(data)
    X(i) = data(i).x;
    Y(i) = data(i).y;
    potential(i) = data(i).potential;
    pixel(i) = data(i).pixel;
    sinus(i) = readSinus(data(i).sinus);
end

Z = (pixel + potential) .* sinus;

scatter(X,Y,25,Z, 'filled')