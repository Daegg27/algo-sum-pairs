exports.sumPairs = function(array, desiredSum) {

    let finalArray = [];

    for (let i = 1; i < array.length; i++ )
    { 
        for (let a = i; a < array.length; a++)
        {
            if (array[a] == array[i]) continue; //Skips when number is the same
            if (array[a] + array[i] == desiredSum)
            {
                finalArray.push([array[i], array[a]]);
            }
        }
    }
    if (finalArray[0] === undefined)
    {
        return "unable to find pairs";
    }
    else{
        return finalArray;
    }
        
        

};
// console.log(exports.sumPairs([1,2,3,4,5], 9));
// console.log(exports.sumPairs([1,2,3,4,5], 7));
// console.log(exports.sumPairs([3, 1, 5, 8, 2], 27));



