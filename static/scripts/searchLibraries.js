
        const searchInputLib = document.getElementById('searchInputLibs');
        const searchResultsLib = document.getElementById('searchResultsLibs');

        async function loadPageLib() {
            const response = await fetch('/searchl', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                }
            });

            const data = await response.json();
            const libraries = data.libraries;
            searchResultsLib.innerHTML = libraries.map(library => {
                return (
                    `<div class="col-lg-3 col-md-4 col-sm-6 product-card">
                <div class="card">
                    <img class="card-img-top product-image"
                        src="/static/${library.img}" alt="Product Image">
                    <div class="card-body">
                        <h5 class="card-title">${library.name}</h5>
                        <p class="card-text">${library.description}</p>
                        <a class="btn btn-primary" href="/library/${ library.id }">ნახვა</a>
                        <a class="btn btn-primary" >ადმინი: ${library.admin} </a>
                    </div>
                </div>
            </div>`
                );
            }).join('');
        }

        loadPageLib();
        searchInputLib.addEventListener('input', async () => {
            const query = searchInputLib.value.trim();

            if (query.length >= 1) {
                const response = await fetch('/searchl', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                    },
                    body: `query=${encodeURIComponent(query)}`,
                });

                const data = await response.json();
                const libraries = data.libraries;

                // Update the results
                searchResultsLib.innerHTML = libraries.map(library => {
                    return (
                        `<div class="col-lg-3 col-md-4 col-sm-6 product-card">
                <div class="card">
                    <img class="card-img-top product-image"
                        src="/static/${library.img}" alt="Product Image">
                    <div class="card-body">
                        <h5 class="card-title">${library.name}</h5>
                        <p class="card-text">${library.description}</p>
                        <a class="btn btn-primary" href="library/{{ library.LibID }}">ნახვა</a>
                        <a class="btn btn-primary" href="delete_library/{{ library.LibID }}">წაშლა</a>
                    </div>
                </div>
            </div>`
                    );
                }).join('');
            } else {
                // Load the page again if the query is too short
                loadPageLib();
            }
        });