import java.io.*;
import java.util.*;

import org.dblp.mmdb.Field;
import org.dblp.mmdb.JournalTitle;
import org.dblp.mmdb.Person;
import org.dblp.mmdb.PersonName;
import org.dblp.mmdb.Publication;
import org.dblp.mmdb.RecordDb;
import org.dblp.mmdb.RecordDbInterface;
import org.dblp.mmdb.TableOfContents;
import org.xml.sax.SAXException;


@SuppressWarnings("javadoc")
class Parser {
    public static void main(String[] args) {
        System.setProperty("entityExpansionLimit", "10000000");

        if (args.length != 2) {
            System.err.format("Usage: java %s <dblp-xml-file> <dblp-dtd-file>\n", Parser.class.getName());
            System.exit(0);
        }
        String dblpXmlFilename = args[0];
        String dblpDtdFilename = args[1];

        System.out.println("building the dblp main memory DB ...");
        RecordDbInterface dblp;
        try {
            dblp = new RecordDb(dblpXmlFilename, dblpDtdFilename, false);
        }
        catch (final IOException ex) {
            System.err.println("cannot read dblp XML: " + ex.getMessage());
            return;
        }
        catch (final SAXException ex) {
            System.err.println("cannot parse XML: " + ex.getMessage());
            return;
        }
        System.out.format("MMDB ready: %d publs, %d pers\n\n", dblp.numberOfPublications(), dblp.numberOfPersons());

        // write the journals into a file
        String journalFileName = "raw_dblp_venues.txt";
        try {
            BufferedWriter writer = new BufferedWriter(new FileWriter(journalFileName));
            for(JournalTitle jt : dblp.getJournals()) {
                writer.write(jt.getTitle().toLowerCase()+"\n");
            } 
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
