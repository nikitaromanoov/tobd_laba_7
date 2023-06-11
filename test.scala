import java.time.format.{DateTimeFormatter, FormatStyle}
import java.time.LocalDate
import java.util.Locale._
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions.col

object FrenchDate {
  def main(args: Array[String]): Unit = {

    
  
    val spark = SparkSession.builder()
        .appName("Creating DataFrame")
        .master("local[*]")
        .getOrCreate()

    val df = spark.read
        .option("header", "true")
        .option("sep", "\t")
        .csv("/app/showcase/data.csv")
    
    val columns = df.columns
    val good_columns =  columns.filter(x => x.contains("100g"))



    println(good_columns (0))
    println(good_columns (1))
    println(good_columns (2))
    val result = good_columns.map(x => col(x).cast("float"))
    val df_1 = df.select(good_columns.map(x => col(x).cast("float")): _*)
    val df_2 =  df_1.na.fill(0.0).na.fill("unk")
    
    df_2.coalesce(1).write.mode("overwrite").option("header","true")
    .option("delimiter","\t")
    .csv("/app/showcase/data_preprocessed.csv")
    
    spark.stop;

  }
}
