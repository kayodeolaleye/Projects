import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Locale;

public class Project {

    // This Java program is used to create a project object.

    // Attributes

    int projNum;
    String projName;
    String projType;
    String projLocation;
    String ERFNum;
    double projFee;
    double feesPaid;
    String projDeadline;
    String contractorDetails;
    String architectDetails;
    String customerDetails;
    String status;
    String completionDate;
    
    // Constructors

    public Project(int projNum, String projName, String projType, String projLocation, String ERFNum, double projFee, 
        double feesPaid, String projDeadline, String contractorDetails, String architectDetails, String customerDetails) {

        this.projNum = projNum;
        this.projName = projName;
        this.projType = projType;
        this.projLocation = projLocation;
        this.ERFNum = ERFNum;
        this.projFee = projFee;
        this.feesPaid = feesPaid;
        this.projDeadline = projDeadline;
        this.contractorDetails = contractorDetails;
        this.architectDetails = architectDetails;
        this.customerDetails = customerDetails;
        this.status = "";
        this.completionDate = "";

    }

    // Methods

    public String captureProjectDetails(String name) {

        //This method captures the detaiils of a project and returns the information as a string
        String projDetails = "";
        if (projName == "") {
            projName = name;
            projDetails += projType + " " + projName + " Information";
        }
       
        projDetails += "\n------------------------------------------------------------";
        projDetails += "\n" + projType + " Number: " + projNum;
        projDetails += "\n" + projType + " Location: " + projLocation;
        projDetails += "\n" + projType + " ERF Number: " + ERFNum;
        projDetails += "\n" + projType + " Fee: " + projFee;
        projDetails += "\nPaid: " + feesPaid;
        projDetails += "\nProject Deadline: " + projDeadline;
        projDetails += "\nContractor: " + contractorDetails;
        projDetails += "\nArchitect: " + architectDetails;
        projDetails += "\nCustomer: " + customerDetails;
        

        if (status != "" && completionDate != "") {
            projDetails += "\nCompletion Date: " + completionDate;
            projDetails += "\nProject Status: " + status;
        }

        projDetails += "\n------------------------------------------------------------\n";

        return projDetails;
    }

    public void changeDate(String dateStr) {

        // Convert dates in String to a LocalDate object
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("YYYY-MM-DD", Locale.ENGLISH);
        LocalDate oldDate = LocalDate.parse(projDeadline, formatter);
        LocalDate newDate = LocalDate.parse(dateStr, formatter);

        LocalDate currentDate = LocalDate.now();
        if (oldDate != newDate) {
            
            projDeadline = dateStr;
        }

        if (newDate.compareTo(currentDate) < 0) {
            
            System.out.println("" + dateStr + " is before today's date");

        }

        System.out.println("Project due date successfully changed to " + newDate + "!");

    }

    public void updateFeePaid(double amount) {
        
        // This method change the value stored in feesPaid by adding amount to feesPaid

        double newPaid = feesPaid + amount;
        feesPaid = newPaid;

    }

    public String finaliseProject() {
        
        // This method returns details of the customer of a project and the amount yet to be paid by the customer. If the 
        // customer has already paid the full fee, an empty String is returned.
        completionDate = LocalDate.now().toString();
        status = "Finalised";
        double balancePayment = projFee - feesPaid;
        String invoice = customerDetails;
        invoice += "\n-------------------------------------------------";
        invoice += "\nProject fee: " + projFee;
        invoice += "\nAmount paid: " + feesPaid;
        invoice += "\nBalance payment: " + balancePayment;
        invoice += "\n-------------------------------------------------";

        if (balancePayment > 0) {
            
            return invoice;

        } else {

            invoice = "";

            return invoice;

        }

        

        


    }
    
}