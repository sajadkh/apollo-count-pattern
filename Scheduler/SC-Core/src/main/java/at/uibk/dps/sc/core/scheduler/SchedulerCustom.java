package at.uibk.dps.sc.core.scheduler;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import org.opt4j.core.start.Constant;
import com.google.inject.Inject;
import com.google.gson.JsonObject;
import com.google.gson.JsonElement;
import com.google.inject.Singleton;
import at.uibk.dps.ee.guice.starter.VertxProvider;
import at.uibk.dps.ee.model.graph.SpecificationProvider;
import at.uibk.dps.sc.core.capacity.CapacityCalculator;
import at.uibk.dps.ee.model.properties.PropertyServiceFunction;
import at.uibk.dps.ee.model.properties.PropertyServiceMapping;
import at.uibk.dps.ee.model.properties.PropertyServiceData;
import at.uibk.dps.ee.model.properties.PropertyServiceMapping.EnactmentMode;
import at.uibk.dps.ee.model.utils.UtilsEnactmentGraph;
import net.sf.opendse.model.Mapping;
import net.sf.opendse.model.Resource;
import net.sf.opendse.model.Task;

/**
 * The {@link SchedulerCustom} randomly picks a (non-unique) subcollection of
 * given size from the mappings available for a user task.
 * 
 * @author Fedor Smirnov
 */
@Singleton
public class SchedulerCustom extends SchedulerAbstract {

    protected EnactmentMode preferedEM = EnactmentMode.Local;
    protected boolean preferedEMIsUpdated = false;
  /**

   * The injection constructor.
   * 
   * @param specProvider the specification provider
   */
  @Inject
  public SchedulerCustom(final SpecificationProvider specProvider,
      final CapacityCalculator capCalc, final VertxProvider vProv) {
    super(specProvider, capCalc, vProv);
  }

  @Override
  protected Set<Mapping<Task, Resource>> chooseMappingSubset(final Task task,
      final Set<Mapping<Task, Resource>> mappingOptions) {

    final List<Mapping<Task, Resource>> mappingList = new ArrayList<>(mappingOptions);
    Set<Mapping<Task, Resource>> filteredMappingList =  mappingList.stream()
        .filter(mapping -> !excludeMapping(mapping, task, this.getPreferedEnactmentMode(task))).collect(Collectors.toSet());

    return filteredMappingList;
  }

  /**
   * Returns true if mapping type be equal with prefered EnactmentMode
   * 
   * @param mapping the given mapping
   * @return Returns true if mapping type be equal with prefered EnactmentMode
   */
  protected boolean excludeMapping(final Mapping<Task, Resource> mapping, final Task process, final EnactmentMode preferedEM) {
    return !PropertyServiceMapping.getEnactmentMode(mapping).equals(preferedEM);
  }
  protected EnactmentMode getPreferedEnactmentMode(Task task){
    // boolean isRoot = PropertyServiceData.isRoot(task);
    if(!this.preferedEMIsUpdated) {
        Set<Task> nonConstantRoots = UtilsEnactmentGraph.getNonConstRootNodes(specification.getEnactmentGraph());
        List<Task> txtInputArr = nonConstantRoots.stream().filter(node -> PropertyServiceData.getJsonKey(node).equals("s")).collect(Collectors.toList());
        String text = PropertyServiceData.getContent(txtInputArr.get(0)).toString();
        List<Task> wordPerBatchInputArr = nonConstantRoots.stream().filter(node -> PropertyServiceData.getJsonKey(node).equals("w")).collect(Collectors.toList());
        String wordPerBatchStr = PropertyServiceData.getContent(wordPerBatchInputArr.get(0)).toString();
        Integer wordPerBatch = Integer.parseInt(wordPerBatchStr);

        this.preferedEM = this.getPreferedEnactmentMode(text, wordPerBatch);
        this.preferedEMIsUpdated = true;
    }
    System.out.println(this.preferedEM);
    return this.preferedEM;
  }
  protected EnactmentMode getPreferedEnactmentMode(String str, int wordPerBatch){
    int wordCount = countWords(str);
    double batchSize = Math.ceil((double)wordCount/wordPerBatch);
    System.out.println(wordCount);
    System.out.println(batchSize);
    if(batchSize < 10.0){
        return EnactmentMode.Local;
    }
    else {
        return EnactmentMode.Serverless;
    }
  }

  protected int countWords(String s){
        int wordCount = 0;

        boolean word = false;
        int endOfLine = s.length() - 1;

        for (int i = 0; i < s.length(); i++) {
            // if the char is a letter, word = true.
            if (Character.isLetter(s.charAt(i)) && i != endOfLine) {
                word = true;
                // if char isn't a letter and there have been letters before,
                // counter goes up.
            } else if (!Character.isLetter(s.charAt(i)) && word) {
                wordCount++;
                word = false;
                // last word of String; if it doesn't end with a non letter, it
                // wouldn't count without this.
            } else if (Character.isLetter(s.charAt(i)) && i == endOfLine) {
                wordCount++;
            }
        }
        return wordCount;
    }
}
