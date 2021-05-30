function [output] = readSinus(value)
output = 0.5;

try
    tag = value.py_reduce{2, 1}.py_tuple{1};
    if strcmp(tag, 'KET')
        output = 0.6;
    elseif strcmp(tag, 'LIB')
        output = 1;
    elseif strcmp(tag, 'PER')
        output = 1;
    elseif strcmp(tag, 'EPE')
        output = 1.1;
    elseif strcmp(tag, 'PRA')
        output = 0.9;
    elseif strcmp(tag, 'SQK')
        output = 1.1;
    elseif strcmp(tag, 'PRE')
        output = 0.6;
    elseif strcmp(tag, 'BUM')
        output = 0.6;
    elseif strcmp(tag, 'TRA')
        output = 0.6;
    elseif strcmp(tag, 'HED')
        output = 1.1;
    end
catch ME
   warning('Problem using function.  Assigning a value of 0.');
end
    
end

