var faker = require("faker")
function generateAddress() {
    console.log(faker.internet.email());
    console.log(faker.address.city());
    console.log(faker.address.streetAddress());
    console.log(faker.address.state());
} 
generateAddress();




