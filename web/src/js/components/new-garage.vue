<template>
    <div>
        <div class="row">
            <label class="col-sm-4">Name</label>
            <input type="text" class="col-sm-8" v-model="garage.name"/>
        </div>
        <div class="row">
            <label class="col-sm-4">Brand</label>
            <input type="text" class="col-sm-8" v-model="garage.brand"/>
        </div>
        <div class="row">
            <label class="col-sm-4">Country</label>
            <input type="text" class="col-sm-8" v-model="garage.postal_country"/>
        </div>
        <div class="row">
            <button class="pull-right btn btn-success" @click="save">Save</button>
        </div>
    </div>
</template>

<script>
    export default {
        name: "new-garage",
        data() {
            return {
                garage: {
                    name: '',
                    brand: '',
                    postal_country: ''
                }
            }
        },
        methods: {
            save() {
                console.log(this.garage)
                $.ajax({
                    type: 'POST',
                    url: `/garages/`,
                    contentType: 'application/json',
                    data: JSON.stringify(this.garage),
                    timeout: 2000
                }).then((data) => {
                    this.$emit('change', data)
                    this.resetForm()
                }).always(() => {
                    // this.loading = false
                })
            },
        }
    }
</script>

<style scoped>

</style>
