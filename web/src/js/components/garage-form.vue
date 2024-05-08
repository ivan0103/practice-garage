<template>
    <div>
        <h3>{{title}}</h3>
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
        name: "garage-form",
        props: {
            garage: {
                type: Object,
                required: false,
                default: ''
            }
        },
        computed: {
            title() {
                return this.garage.id ? 'Edit garage': 'Add new garage'
            },
            name: {
                set(val) {
                    this.garage.name = val
                },
                get() {
                    return this.garage.name
                }
            }
        },
        data() {
            return {
                myGarage: {}
            }
        },
        mounted() {
            console.log(JSON.stringify(this.garage))
            Object.assign(this.myGarage, this.garage)
        },
        methods:{
            save() {
                if (this.garage.id) {
                    Object.assign(this.myGarage, this.garage)
                }
                $.ajax({
					type: this.myGarage.id ? 'PUT':'POST',
					url: `/garages/`,
					contentType: 'application/json',
                    data: JSON.stringify(this.myGarage),
					timeout: 2000
				}).then((data) => {
                    this.$emit('change', data)
                    if (this.garage.id === undefined){
                        this.resetForm()
                    }
				}).always(() => {
					// this.loading = false
				})
            },
            resetForm() {
                if (this.garage.id) {
                    Object.assign(this.myGarage, this.garage)
                } else {
                    this.myGarage = {
                        name: '',
                        brand: '',
                        postal_country: ''
                    }
                    Object.assign(this.garage, this.myGarage)
                }
            },

        },
        watch: {
        }
    }
</script>

<style scoped>

</style>