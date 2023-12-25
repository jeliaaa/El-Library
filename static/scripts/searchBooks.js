
        const searchInput = document.getElementById('searchInput');
        const searchResults = document.getElementById('searchResults');

        async function loadPage() {
            const response = await fetch('/searchb', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                }
            });

            const data = await response.json();
            const books = data.books;
            searchResults.innerHTML = books.map(book => {
                return (
                    `<div class="card" style="width: 18rem;">
                        <img src="/static/${book.img}" class="card-img-top" alt="...">
                        <div class="card-body">
                            <h5 class="card-title">${book.name}</h5>
                            <p class="card-text">${book.description}</p>
                        </div>
                        <div class="card-body">
                            <p class="card-link">${book.author}</p>
                        </div>
                    </div>`
                );
            }).join('');
        }

        // Call the loadPage function on page load
        loadPage();

        searchInput.addEventListener('input', async () => {
            const query = searchInput.value.trim();

            if (query.length >= 1) {
                const response = await fetch('/searchb', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                    },
                    body: `query=${encodeURIComponent(query)}`,
                });

                const data = await response.json();
                const books = data.books;

                // Update the results
                searchResults.innerHTML = books.map(book => {
                    return (
                        `<div class="card" style="width: 18rem;">
                            <img src="/static/${book.img}" class="card-img-top" alt="...">
                            <div class="card-body">
                                <h5 class="card-title">${book.name}</h5>
                                <p class="card-text">${book.description}</p>
                            </div>
                            <div class="card-body">
                                <a href="/delete_book/${book.BookID}" class="card-link">${book.author}</a>
                            </div>
                        </div>`
                    );
                }).join('');
            } else {
                // Load the page again if the query is too short
                loadPage();
            }
        });