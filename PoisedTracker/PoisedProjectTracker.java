/**
 * PoisedProjectTracker
 */
public class PoisedProjectTracker {

    // This Java program helps a company Poised to keep track of projects.
    
    public static void main(String[] args) {
   
        // Person objects
        Person customer = new Person("Mike", "Tyson", "+1254856456", "mike@tyson.com", "Okhlahoma");
        Person architect = new Person("Wallace", "Kiyosaki", "+11545564646", "wallace@poised.co.za", "Cape Town");
        Person contractor = new Person("Dave", "Nicholas", "+115585564646", "dave@poised.co.za", "Cape Town");
        // Project objects
        Project house = new Project(1, "", "House", "Okhlahoma", "ERF78545", 78585.52, 74000.0, "2021-08-19", contractor.getPersonDetails(),
         architect.getPersonDetails(), customer.getPersonDetails());

        System.out.println("Printing Project Details...");
        System.out.print(house.captureProjectDetails(customer.getLastName()));
        System.out.println("Finalising Project...");
        System.out.println(house.finaliseProject());
        System.out.println("Project Finalised Successfully");
  
        System.out.println("Printing Finalised Project Details...");
        System.out.println(house.captureProjectDetails(customer.getLastName()));
    }
    
}