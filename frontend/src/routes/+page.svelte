<script>
	let file;
	let mongodbLink = '';
	let collection = '';
	let db = '';

	async function processForm() {
		if (!file || mongodbLink == '' || collection == '' || db == '') {
			return;
		}

		const formData = new FormData();
		formData.append('file', file);
		formData.append('mongodb-link', mongodbLink);
		formData.append('collection', collection);
		formData.append('db-name', db);

		try {
			const response = await fetch('http://127.0.0.1:5000/upload', {
				method: 'POST',
				body: formData
			});

			if (response.ok) {
				const result = await response.json();
				console.log(result);
			} else {
				const error = await response.text();
				console.error(error);
			}
		} catch (error) {
			console.error(error);
		}
	}
</script>

<form method="POST" enctype="multipart/form-data">
	<input
		type="file"
		name="file"
		accept=".xls,.xlsx"
		required
		on:change={(e) => (file = e.target.files[0])}
	/>
	<input
		type="text"
		name="mongodb-link"
		placeholder="mongodb uri"
		autocomplete="off"
		class="border-1 my-4 block rounded-md border px-2 py-1"
		required
		bind:value={mongodbLink}
	/>
	<input
		type="text"
		name="collection"
		placeholder="collection name"
		autocomplete="off"
		class="border-1 my-4 block rounded-md border px-2 py-1"
		required
		bind:value={collection}
	/>
	<input
		type="text"
		name="collection"
		placeholder="db"
		autocomplete="off"
		class="border-1 my-4 block rounded-md border px-2 py-1"
		required
		bind:value={db}
	/>
	<button
		type="submit"
		on:click|preventDefault={processForm}
		class="my-4 block w-fit rounded-md bg-green-600 px-2 py-1 text-white hover:bg-green-700 active:bg-green-800"
		>Upload</button
	>
</form>
