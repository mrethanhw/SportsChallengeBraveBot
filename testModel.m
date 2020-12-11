%%
load("trainedModel1.mat");
sep_data = readtable("sep_data.csv");
y = trainedModel1.predictFcn(sep_data);
sep_data = readcell("sep_data.csv");
%%
[row column] = size(sep_data);
attendance = cell(row, 1);
attendance{1} = "attendance";
predicted_attendance = cell(row, 1);
predicted_attendance{1} = "predicted_attendance";
percentage_error = cell(row, 1);
percentage_error{1} = "percentage error";
for i = 2:row
    attendance{i} = str2num(erase(sep_data{i, 13}, ','));
    predicted_attendance{i} = y(i-1);
    percentage_error{i} = (predicted_attendance{i} - attendance{i}) / attendance{i} *100;
end
sep_predict = [attendance predicted_attendance percentage_error];
writecell(sep_predict, "sep_predict.csv");