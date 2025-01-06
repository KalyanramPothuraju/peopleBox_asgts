function convertToCamelCase(obj) {
    
    // let result = {}; Create a new object to store the result

    // Iterate through each key in the original object
    for (let key in obj) {
        if (obj.hasOwnProperty(key)) {
            // Convert the key from snake_case to camelCase
            let camelCaseKey = key.replace(/_([a-z])/g, (match, letter) => letter.toUpperCase());

            // Add the key-value pair to the result object
            result[camelCaseKey] = obj[key];
        }
    }

    return result;
}

// Example usage:
const snakeCaseObject = {
    "first_name": "John",
    "last_name": "Doe",
    "email_address": "john.doe@example.com"
};

const camelCaseObject = convertToCamelCase(snakeCaseObject);
console.log(camelCaseObject);
