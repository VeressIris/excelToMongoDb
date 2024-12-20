<script>
	let file;
	let sheetsLink = '';
	let mongodbLink = '';
	let collection = '';
	let db = '';
	let fileMessage = '';

	async function processForm() {
		if (!file || mongodbLink == '' || collection == '' || db == '' || sheetsLink == '') {
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

<div class="flex flex-col items-center justify-center">
	<h1 class="mb-6">Google Sheets to <span class="text-green-700">MongoDB</span> converter</h1>
	<form
		method="POST"
		enctype="multipart/form-data"
		class="flex flex-col items-center justify-center rounded-2xl bg-white text-center text-lg"
	>
		<div class="flex w-full flex-col items-start">
			<label for="sheets-link" class="font-bold">Google Sheets link:</label>
			<input
				type="text"
				name="sheets-link"
				placeholder="google sheets link"
				autocomplete="off"
				class="duration-250 mb-3 w-full rounded-md border-[1.5px] border-black p-3 text-base shadow-[2.5px_3px_0_#000] outline-none transition-shadow focus:shadow-[5.5px_7px_0_#000]"
				required
				bind:value={sheetsLink}
			/>
			<label for="mongodb-link" class="font-bold">MongoDB URI:</label>
			<input
				type="text"
				name="mongodb-link"
				placeholder="mongodb uri"
				autocomplete="off"
				class="duration-250 mb-3 w-full rounded-md border-[1.5px] border-black p-3 text-base shadow-[2.5px_3px_0_#000] outline-none transition-shadow focus:shadow-[5.5px_7px_0_#000]"
				required
				bind:value={mongodbLink}
			/>
			<label for="collection" class="font-bold">Collection name:</label>
			<input
				type="text"
				name="collection"
				placeholder="ex: users"
				autocomplete="off"
				class="duration-250 mb-3 w-full rounded-md border-[1.5px] border-black p-3 text-base shadow-[2.5px_3px_0_#000] outline-none transition-shadow focus:shadow-[5.5px_7px_0_#000]"
				required
				bind:value={collection}
			/>
			<label for="db" class="font-bold">Database name:</label>
			<input
				type="text"
				name="db"
				placeholder="ex: db"
				autocomplete="off"
				class="duration-250 mb-3 w-full rounded-md border-[1.5px] border-black p-3 text-base shadow-[2.5px_3px_0_#000] outline-none transition-shadow focus:shadow-[5.5px_7px_0_#000]"
				required
				bind:value={db}
			/>
		</div>
		<button
			type="submit"
			on:click={processForm}
			class="my-2 block w-fit rounded-md bg-green-700 px-3 py-2 text-xl font-semibold text-white outline-green-100 transition-all hover:bg-green-800 hover:outline hover:outline-4 active:bg-green-900"
			>Upload</button
		>
	</form>
</div>
