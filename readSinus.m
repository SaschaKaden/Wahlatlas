function [output] = readSinus(tag)
tag = string(tag);

if contains(tag, 'KET')
    output = 0.6;
elseif contains(tag, 'LIB')
    output = 1;
elseif contains(tag, 'PER')
    output = 1;
elseif contains(tag, 'EPE')
    output = 1.1;
elseif contains(tag, 'PRA')
    output = 0.9;
elseif contains(tag, 'SQK')
    output = 1.1;
elseif contains(tag, 'PRE')
    output = 0.6;
elseif contains(tag, 'BUM')
    output = 0.6;
elseif contains(tag, 'TRA')
    output = 0.6;
elseif contains(tag, 'HED')
    output = 1.1;
else
    output = 0.5;
end
    
end

