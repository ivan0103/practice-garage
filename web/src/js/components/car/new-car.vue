<template>
    <div>
        <div class="row">
            <label class="col-sm-4">Plate</label>
            <input type="text" class="col-sm-8" v-model="car.plate"/>
        </div>
        <div class="row">
            <label class="col-sm-4">Brand</label>
            <input type="text" class="col-sm-8" v-model="car.brand"/>
        </div>
        <div class="row">
            <button class="pull-right btn btn-success" @click="add">Add</button>
        </div>
    </div>
</template>

<script>
    export default {
        name: "new-car",
        props: {
            garageId: {
                type: [Number, String], // Accepts both number and string
                required: true
            }
        },
        data() {
            return {
                car: {
                    plate: '',
                    brand: '',
                }
            }
        },
        methods: {
            add() {
                $.ajax({
                    type: 'POST',
                    url: `/garages/${this.garageId}/cars`,
                    contentType: 'application/json',
                    data: JSON.stringify(this.car),
                    timeout: 2000
                }).then((data) => {
                    this.$emit('add', data)
                    this.resetForm()
                }).always(() => {
                    // this.loading = false
                })
            },
        },
    }
</script>

<style scoped>

</style>