public class Person {

    // This Java program is used to create a person object

    //Attributes
    String firstName;
    String lastName;
    String phoneNum;
    String email;
    String address;

    // Constructors
    public Person(String firstName, String lastName, String phoneNum, String email, String address) {

        this.firstName = firstName;
        this.lastName = lastName;
        this.phoneNum = phoneNum;
        this.email = email;
        this.address = address;
    }

    // Methods

    public String getLastName() {

        return lastName;
    }

    public void updateContactDetails(String newPhoneNum, String newAddress) {

        // This method takes two String arguments: a new phone number and a new address and use them to replace the 
        // value stored in phoneNum and address

        if (newPhoneNum != phoneNum) {
            
            phoneNum = newPhoneNum;
        }

        if (newAddress != address) {
            
            address = newAddress;
        }

        System.out.println("Contact details successfully updated!");

    }

    public String getPersonDetails() {

        String details = "" + firstName + " " + lastName + ", Phone Number: " + phoneNum + ", Email: " + email + ", Address: " + address;

        return details;
    }
    
    
}