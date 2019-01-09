Zadanie projektowe na przedmiot *Matematyczne Metody Wspomagania Decyzji*.

Projekt polega na rozwiązaniu problemu rozmieszczenia fabryk, aby koszt tranportu różnego rodzaju przedmiotów między nimi był minimalny (jest to przykład probelmu QAP). Zadanie rozwiązujemy przy pomocy algorytmu genetycznego.

Skrypty zostały napisanie w wersji 3.7 Pythona. Skorzystaliśmy również z biblioteki Numpy oraz Matplotlib. Do uruchomienia projektu potrzebny jest komputer z interpreterem Pythona 3.7 oraz zainstalowanymi wcześniej wymienionymi bibliotekami.

W pliku input_data.txt można wybrać parametry algorytmu oraz ścieżki do danych wejściowych (macierzy odległości i przepływu zapisanych w plikach .csv). Następnie w celu uruchomienia algorytmu należy wywołać skrypt algorithm_v3.py. Po zakończeniu działania algorytmu, w konsoli wypisywane jest najlepsze znalezione rozwiązanie, wartość jego funkcji celu, a także otwiera się okienko z wykresem przedstawiającym przebieg działania algorytmu.

Zaimplementowaliśmy operatory:
  * selekcji: proporcjonalnej, turniejowej, odcinającej
  * krzyżowania: OX, PMX
  * mutacji: swap, inversion, scramble
  * sukcesji: mieszanej, przepuszczającej tylko potomków

Opis poszczególnych funkcji:
 * z pliku generate_new_population.py
   * generate_new_population(population_size, permutation_length) - Funkcja losowo generuje populację startową o zadanej wielkości składającą się z losowych permutacji o zadanej długości.
   save_population_to_file(population, filename) - Funkcja zapisuje wybraną populację do pliku, umożliwiając skorzystanie z niej w algorytmie głównym.
 * z pliku fitness_function.py
   * fitness_function(solution, transport_cost_matrix, distance_matrix) - Funkcja oblicza wartość funkcji celu danego rozwiązania, uwzględniając macierze odległości oraz kosztów.
   * fit_fun(solution) - Skrócona wersja powyższej funkcji, przyjmująca jako argument tylko rozwiązanie.
 * z pliku crossover_operators.py
   * ox(parent1, parent2) - Funkcja realizująca operator krzyżowania OX - Order Crossover. Jako argumenty przyjmuje dwóch rodziców, zwraca dwóch potomków.
   * pmx(parent1, parent2) - Funkcja realizująca operator krzyżowania PMX - Partially-Mapped Crossover. Jako argumenty przyjmuje dwóch rodziców, zwraca dwóch potomków.
 * z pliku mutation_operators.py
   * inversion_mutation(organism, percentage_of_change) - Funkcja realizująca operator mutacji w sposób inwersji. Z rozwiązania losowo wybierany jest podciąg, w organiźmie po mutacji na jego miejscu widnieje podciąg w odwrotnej kolejności. Jako argumenty funkcja przyjmuje organizm do mutacji oraz maksymalny procentowy wpływ mutacji. Funkcja zwraca organizm po mutacji.
   * scramble_mutation(organism, percentage_of_change) - Funkcja realizująca operator mutacji w sposób przemieszania. Z rozwiązania losowo wybierany jest podciąg, w organizmie po mutacji na jego miejscu widnieje podciąg w losowo ustawionej kolejności. Jako argumenty funkcja przyjmuje organizm do mutacji oraz maksymalny procentowy wpływ mutacji. Funkcja zwraca organizm po mutacji.
   * swap_mutation(organism, percentage_of_change) - Funkcja realizująca operator mutacji w sposób zamiany. Z rozwiązania losowo wybierane są dwa indeksy, w organizmie po mutacji wartości rozwiązania dla tych indeksów są ze sobą zamienione. Jako argumenty funkcja przyjmuje organizm do mutacji. Funkcja zwraca organizm po mutacji.
 * z pliku selection_operators.py
   * proportionate_selection(population, number_of_parents) - Funkcja realizująca operator selekcji w sposób proporcjonalny. Każdemu rozwiązaniu z populacji przypisywane jest prawdopodobieństwo bycia wybranym na rodzica. Prawdopodobieństwo jest proporcjonalne do wartości funkcji celu. Ponieważ algorytm rozwiązuje zagadnienie minimalizacji, do wszystkich wartości funkcji celu rozwiązań dodajemy dwukrotnie różnicę pomiędzy wartością największą, a daną wartością, aby rozwiązanie z początkowo najmniejszą wartością uzyskało wartość największą. Jako argumenty funkcja przyjmuje populację oraz liczbę rodziców do utworzenia. Funkcja zwraca określoną liczbę rodziców.
   * tournament_selection(population, tournament_size) - Funkcja realizująca operator selekcji w sposób turniejowy. Populacja jest ustawiana w losowe grupy o zadanej liczebności, rozwiązanie o najlepszej wartości funkcji celu z każdej grupy jest wybierane na rodzica. Jako argumenty funkcja przyjmuje populację oraz rozmiar grupy turniejowej. Funkcja zwraca listę rodziców.
   * truncation_selection(population, truncation_threshold) - Funkcja realizująca operator selekcji w sposób obcinający. Populacja jest sortowana pod względem wartości funkcji celu, następnie zadany procent najlepszych rozwiązań jest wybierany na rodziców. Jako argumenty funkcja przyjmuje populację oraz procentową wartość odcięcia. Funkcja zwraca listę rodziców.
 * succession_operators.py
   * children_only(size, children) - Funkcja tworząca populację wyłącznie na podstawie listy potomków. Rozwiązania są sortowane pod względem wartości funkcji celu, następnie zadana liczba najlepszych z nich trafia do populacji. Jako argumenty funkcja przyjmuje rozmiar nowej populacji oraz listę potomków. Funkcja zwraca nową populację.
   * mixed(size, children, parents) - Funkcja tworząca populację na podstawie zarówno rodziców jak i potomków.
	Lista rodziców jest dołączana do listy potomków, następnie losowo przestawiana. Zadana liczba rozwiązań trafia do populacji. Jako argumenty funkcja przyjmuje rozmiar nowej populacji, listę potomków oraz listę rodziców. Funkcja zwraca nową populację.

Operatory znajdujące się w jednym pliku przyjmują takie same argumenty, jednak niektóre z nich nie są potrzebne. Jest to spowodowane tym, aby móc łatwo wykorzystywać skrypt algorithm_v3.py dla różnych parametrów algorytmu. Ponadto w pliku input_data.txt powinniśmy wypełnić wszystkie pola, mimo że czasami niektóre z nich nie będą potrzebne (np. procentowy wpływ mutacji nie jest konieczny aby poprawnie wykonać swap, ale mimo to musimy go przesłać, aby program główny algorithm_v3.py był generyczny).
