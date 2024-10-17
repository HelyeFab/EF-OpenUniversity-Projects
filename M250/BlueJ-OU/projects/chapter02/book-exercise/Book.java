/**
 * A class that maintains information on a book.
 * This might form part of a larger application such
 * as a library system, for instance.
 *
 * @author (Insert your name here.)
 * @version (Insert today's date here.)
 */
class Book
{
    // The fields.
    @SuppressWarnings("unused")
    private String author;
    @SuppressWarnings("unused")
    private String title;
    @SuppressWarnings("unused")
    private int pages;

    /**
     * Set the author and title fields when this object
     * is constructed.
     */
    public Book(String bookAuthor, String bookTitle, int bookPages)
    {
        author = bookAuthor;
        title = bookTitle;
        pages = bookPages;
    }

    // Add the methods here ...
    
    public String getAuthor(){
        return author;
    }
      
    public String getTitle(){
        return title;
    }
    
    public int getPages(){
        return pages;
    }
    
    /**
     * Print a ticket if enough money has been inserted, and
     * reduce the current balance by the ticket price. Print
     * an error message if more money is required.
     */
    public void printDetails()
    {
      
            // Simulate the printing of a ticket.
            System.out.println("##################");
            System.out.println("#Book Card#");
            System.out.println("Author: " + author + "###");
            System.out.println("Title: " + title + " ###");
            System.out.println("Pages:" + pages + " ###");
            System.out.println("##################");
            System.out.println();

            
        
    }
    
}
