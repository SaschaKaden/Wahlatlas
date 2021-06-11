% data_dresden = jsondecode(fileread("results/Dresden_250m.json"));
% data_leipzig = jsondecode(fileread("results/Leipzig_500m.json"));
% data_complete = jsondecode(fileread("results/Sachsen_1km.json"));
format compact
data = jsondecode(fileread("Output.json"));
size = length(data);

X = zeros(size,1);
Y = zeros(size,1);
lon = zeros(size,1);
lat = zeros(size,1);
potential = zeros(size,1);
pixel = zeros(size,1);
gru_lt = zeros(size,1);
gru_bt = zeros(size,1);
sinus = zeros(size,1);

divider = 111320;
for i = 1:length(data)
    lon(i) = data(i).lon / divider;
    lat(i) = data(i).lat / divider;
    X(i) = data(i).lon;
    Y(i) = data(i).lat;
    potential(i) = data(i).potential_scale;
    pixel(i) = data(i).pixel;
    gru_lt(i) = data(i).gru_lt;
    gru_bt(i) = data(i).gru_bt;
    sinus(i) = readSinus(data(i).sinus);
end
potential = potential * 5 / 100;
X = ((X - min(X)) / 250)+1;
Y = flip(((Y - min(Y)) / 250)+1);


Z = pixel .* potential .* sinus;

% get best cells
[bestValues, bestIndexes] = maxk(Z,100);
indexes = [X(bestIndexes), Y(bestIndexes), bestValues]



figure(1);
scatter(X, Y, 30, Z, 'filled', 's')
daspect([1 1 1])
axis tight; 


% create matrix with values
lonLatZ = [lon lat Z];
XYZ = [X Y Z];

Z = Z / 1000;
matXYZ = accumarray(XYZ(:,[2 1]), XYZ(:,3));
h = heatmap(matXYZ, 'CellLabelColor','none');
h.Colormap = parula;
filename = 'testdata.xlsx';
writematrix(matXYZ,filename,'Sheet',1);
