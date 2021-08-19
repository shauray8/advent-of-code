public class Counter{
  private int value;
  public void inc(){
    ++value;
  }
  public int getValue(){
    return value;
  }
}

Counter c = new Counter();
c.inc();
int i = c.getValue();
