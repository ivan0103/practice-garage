<template>
	<div class="grid-container">
		<div class="title">
			<h1>Garages</h1>
			<garage-form @change="addGarageToList"></garage-form>

		</div>
		<ul class="list-group">
		    <li v-for="g in garageList" :key="g.id" class="list-group-item">
				<garage-list-item :garage="g" @delete="deleteGarageFromList"></garage-list-item>
			</li>
		</ul>
	</div>
</template>

<script>
    import GarageListItem from "./garage-list-item";
    import GarageForm from "./garage-form";

	export default {
		name: 'garage-list',
		components: {GarageListItem, GarageForm},
		data: function () {
			return {
				garageList: []
			}
		},
		methods: {
			load() {
				$.ajax({
					type: 'GET',
					url: `/garages/`,
					contentType: 'application/json',
					timeout: 60000
				}).then((data) => {
					this.garageList = data
				}).always(() => {
					this.loading = false
				})
			},
			addGarageToList(newGarage) {
                this.garageList.push(newGarage)
            },
			deleteGarageFromList(garageId) {
				const index = this.garageList.findIndex(item => item.id === garageId);
				if (index !== -1) {
					this.garageList.splice(index, 1);
				}
			},
		},
		created: function() {
			this.load();
		}
	}

</script>

<style scoped>
	.grid-container {
		display: grid;
		grid-template-columns: 2fr 6fr;
		grid-gap: 10px;
		grid-auto-rows: min-content;
		grid-template-areas:
			"title garage-list ";
	}

	.title {
        grid-area: title;
		margin-right: 20px;
    }
	.list-group {
        grid-area: garage-list;
    }
    .add-garage {
        margin: 4px;
    }

</style>
